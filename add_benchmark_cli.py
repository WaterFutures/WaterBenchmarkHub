import json
import os
import re
import importlib
import unittest
from pathlib import Path

from epyt_flow.visualization import ScenarioVisualizer, epanet_colors
from epyt_flow.simulation import ScenarioSimulator


BASE_DIR = Path(__file__).resolve().parent

NETWORKS_FILE = BASE_DIR / "src/water_benchmark_hub/networks/networks.py"
TEST_DIRECTORY = BASE_DIR / "tests"
JSON_FILE_PATH = BASE_DIR / "docs/static/database.json"
MD_TEMPLATE_PATH = BASE_DIR / "md_template.md"

FUNCTION_TEMPLATE = """
@meta_data("{identifier_lower}")
class {name}(WaterDistributionNetwork):
    \"\"\"Loader for network {name}\"\"\"

    @staticmethod
    def load(download_dir: str = get_temp_folder(),
             flow_units_id: int = None, verbose: bool = True,
             return_scenario: bool = False):
        f_in = os.path.join(download_dir, "{name}.inp")
        url = "{link}"

        download_if_necessary(f_in, url, verbose)
        if return_scenario:
            return load_inp(f_in, flow_units_id=flow_units_id)
        return f_in

register("{identifier}", {name})
"""

TEST_TEMPLATE = """
def test_{lower}():
    res = load("{identifier}")

    assert isinstance(res.load(download_dir=get_temp_folder()), str)
    assert isinstance(res.load(download_dir=get_temp_folder(), return_scenario=True), ScenarioConfig)
"""


def ask(prompt, required=True):
    """Ask user for input.

    Parameters
    ----------
    prompt : str
        Text shown to the user.
    required : bool, optional
        Whether empty input is allowed.

    Returns
    -------
    str
        User input.
    """
    while True:
        ans = input(prompt + ": ").strip()
        if ans or not required:
            return ans
        print("This field is required.")


def ask_list(prompt):
    """
    Prompt the user for a comma-separated list.

    Parameters
    ----------
    prompt : str
        Prompt shown to the user.

    Returns
    -------
    list[str]
        Parsed list of values.
    """
    txt = ask(prompt + " (comma separated, optional)", required=False)
    return [t.strip() for t in txt.split(",") if t.strip()]


def load_template():
    """
    Load the Markdown template.

    Returns
    -------
    tuple[str, set[str]]
        Template content and placeholder fields.
    """
    with open(MD_TEMPLATE_PATH, "r") as f:
        content = f.read()
    fields = set(re.findall(r"\{(.*?)\}", content))
    return content, fields


def append_to_file(path, content):
    """
    Append content to a file.

    Parameters
    ----------
    path : Path
        Target file.
    content : str
        Content to append.
    """
    with open(path, "a") as f:
        f.write("\n" + content)


def analyse_network(network_id):
    """
    Analyse a water distribution network and generate a topology plot.

    Parameters
    ----------
    network_id : str
        Network identifier.

    Returns
    -------
    tuple[dict, str]
        Topology statistics and HTML image tag.
    """
    from water_benchmark_hub import load
    network = load(network_id)
    f_inp = network.load()

    with ScenarioSimulator(f_inp_in=f_inp) as sim:
        sim.set_demand_sensors(sim.sensor_config.nodes)
        scada = sim.run_simulation(verbose=True)

        out_dir = Path(f"docs/static/benchmarks/{network_id.lower()}")
        out_dir.mkdir(parents=True, exist_ok=True)
        img_path = out_dir / (network_id.replace("-", "_").lower() + "_plot.png")

        topo = sim.get_topology()
        d = {
            "nodes": len(topo.get_all_nodes()),
            "pipes": len(topo.get_all_pipes()),
            "pumps": len(topo.get_all_pumps()),
            "tanks": len(topo.get_all_tanks()),
            "reservoirs": len(topo.get_all_reservoirs()),
            "valves": len(topo.get_all_valves()),
        }

        dpi = 150
        if d["nodes"] > 1000:
            dpi = 250
        ScenarioVisualizer(sim, color_scheme=epanet_colors).show_plot(export_to_file=str(img_path), dpi=dpi, suppress_plot=True)
        print("Network plotted at:", img_path)

        dur = sim.epanet_api.get_simulation_duration()
        d["pattern"] = dur

        return d, f"<img src=\"../static/benchmarks/{network_id.lower()}/{img_path.name}\"/>"


def save_md(network_id, full_name, long_desc, arch_text, img_link, references):
    """
    Generate and save the markdown file corresponding to a benchmark network.

    This function loads a markdown template, fills it with network specific
    data and writes it to the correct benchmarks documentation directory.

    The output file is named according to the network identifier and
    stored under ``docs/_benchmarks/``.

    Parameters
    ----------
    network_id : str
        Unique identifier of the network
    full_name : str
        Full name of the network
    long_desc : str
        Detailed description of the network
    arch_text : str
        Generated description of the network architecture (nodes, pipes,
        tanks, pumps, etc.)
    img_link : str
        Path to the image of the network topology
    references : str
        String containing the benchmark's references
    """
    template, fields = load_template()

    name = network_id.split("-")[-1]
    out_path = f"docs/_benchmarks/network-{name}.md"

    md = template.format(
        network_id=network_id,
        full_name=full_name,
        long_description=long_desc,
        networks_architecture_description=arch_text,
        image_link=img_link,
        references=references,
        network_id_lower=network_id.lower(),
        name=name,
        name_lower=name.lower(),
    )

    with open(out_path, "w") as f:
        f.write(md)

    print("Markdown written to:", out_path)


def update_json(full_name, desc, year, keywords, doi, license_type,
                link, external_url, network_id, tags):
    """
    Update the benchmark metadata JSON file with a new network entry.

    This function loads the existing JSON metadata file and inserts a new
    benchmark entry to it.

    Parameters
    ----------
    full_name : str
        Full name of the network
    desc : str
        Short description of the network
    year : str or int
        Year of publication.
    keywords : list[str]
        List of keywords describing the network
    doi : str or None
        DOI associated with the network dataset or publication
    license_type : str or None
        License under which the network is distributed
    link : str
        Direct download URL for the network data
    external_url : str or None
        Optional external webpage related to the network
    network_id : str
        Unique identifier of the network
    tags : list[str]
        Classification tags (e.g. size, components, demand patterns)

    """
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, "r") as f:
            data = json.load(f)
    else:
        data = {"tags": {}, "resources": {}}

    permalink = f"benchmarks/network-{network_id.split('-')[-1]}.html"

    data["resources"][network_id.lower()] = {
        "name": full_name,
        "desc": desc,
        "year": year,
        "tags": tags,
        "keywords": keywords,
        "doi": doi,
        "license": license_type,
        "download_url": link,
        "external_url": external_url,
        "permalink": permalink,
    }

    with open(JSON_FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("JSON updated")


def run_test(network_id):
    """
    Execute the unit test associated with a specific network.

    This function imports the network test module and executes the network
    specific test function.

    Parameters
    ----------
    network_id : str
        Unique identifier of the network

    Returns
    -------
    bool
        True if the test exists and passed successfully, False otherwise

    """

    if not network_id:
        print("Network identifier must be filled to run the test!\n")
        return False

    test_function_name = f"test_{network_id.split('-')[-1].lower()}"
    test_file_name = "test_networks"

    test_file_path = os.path.join(TEST_DIRECTORY, f"{test_file_name}.py")
    if not os.path.exists(test_file_path):
        print(f"Test file not found at: {test_file_path}\n")
        return False

    try:
        module_name = f"tests.{test_file_name}"
        test_module = importlib.import_module(module_name)

        test_func = getattr(test_module, test_function_name, None)

        if test_func is None:
            print(f"Test function {test_function_name} not found in {test_file_name}\n")
            return False

        test_case = unittest.FunctionTestCase(test_func)
        result = unittest.TextTestRunner().run(test_case)

        if result.wasSuccessful():
            print(f"Test passed: {test_function_name}\n")
            return True
        else:
            print(f"Test failed: {test_function_name}\n")
            return False

    except Exception as e:
        print(f"An error occurred: {e}\n")
        return False


def main():
    """
    This is the workflow guiding a user through adding a new benchmark entry
    via a command line interface.
    """
    print("\nAdding new benchmark\n")

    network_id = ask("Network short ID (e.g. BAK or KY13)")
    network_id = "Network-" + network_id

    link = ask("Download link")
    full_name = ask("Full network name")
    desc = ask("Short description")
    long_desc = ask("Long description (multi-sentence)")
    year = ask("Year")
    doi = ask("DOI (optional)", required=False)
    keywords = ask_list("Keywords")
    license_type = ask("License (optional)", required=False)
    external_url = ask("External URL (optional)", required=False)

    references = []
    print("\nAdd references (empty to stop):")
    while True:
        ref = ask("Reference text", required=False)
        if not ref:
            break
        doi_ref = ask("Reference DOI", required=False)
        references.append({"text": ref, "doi": doi_ref})

    ref_html = ""
    for r in references:
        if r["text"] and r["doi"]:
            ref_html += f"{r['text']}\n[<i class=\"bi bi-link\"></i>]({r['doi']})\n\n"

    loader_code = FUNCTION_TEMPLATE.format(
        identifier=network_id,
        identifier_lower=network_id.lower(),
        name=network_id.split("-")[-1],
        link=link,
    )
    append_to_file(NETWORKS_FILE, loader_code)
    print("Added loader function")

    print("\nRunning network analysis")
    topo, img_link = analyse_network(network_id)

    arch_parts = []
    for k, v in topo.items():
        if k != "pattern" and v > 0:
            arch_parts.append(f"{v} {k}")
    arch_text = "The network consists of " + ", ".join(arch_parts) + "."

    if topo["pattern"] > 0:
        arch_text += f" It contains a demand pattern of {topo['pattern']} seconds."

    tags = []
    if topo["valves"] > 0: tags.append("valves")
    if topo["tanks"] > 0: tags.append("tanks")
    if topo["pumps"] > 0: tags.append("pumps")

    if topo["nodes"] > 1000:
        tags.append("large")
    elif topo["nodes"] > 100:
        tags.append("medium")
    else:
        tags.append("small")

    if topo["pattern"] > 0:
        tags.append("demand patterns")

    test_code = TEST_TEMPLATE.format(
        identifier=network_id,
        lower=network_id.split("-")[-1].lower(),
    )
    append_to_file(os.path.join(TEST_DIRECTORY, "test_networks.py"), test_code)
    print("Added test function")

    test_success = run_test(network_id)

    if test_success:
        save_md(network_id, full_name, long_desc, arch_text, img_link, ref_html)

        update_json(full_name, desc, year, keywords, doi, license_type,
                    link, external_url, network_id, tags)

        print("\nFinished adding the network successfully")
    else:
        print("Failed test, therefore did not update json and create md. "
              "Please check code manually")


if __name__ == "__main__":
    main()
