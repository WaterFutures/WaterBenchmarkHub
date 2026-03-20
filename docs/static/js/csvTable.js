"use strict";

function insertTable(tableDivId, url, caption) {
    if (caption == undefined) {
        caption = "";
    }

    function processData(csv) {
        var data = csv.split(/\r\n|\n/).map(v => v.split(','));

        var headers = data.shift();

        var table = document.createElement('table');
        table.classList.add("table");
        table.classList.add("table-striped");

        var cap = document.createElement('caption');
        cap.innerHTML = caption + `<a href="${url}" class="btn btn-link"><i class="bi bi-download"></i> Download</a>`;
        table.appendChild(cap);

        var thead = document.createElement('thead');
        table.appendChild(thead);

        thead.innerHTML = '<tr><th>' + headers.join('</th><th>') + '</th></tr>';

        var tbody = document.createElement('tbody');
        table.appendChild(tbody);

        for (var row of data) {
            if (row != "") {
                tbody.innerHTML += '<tr><td>' + row.join('</td><td>') + '</td></tr>';
            }
        }

        document.getElementById(tableDivId).appendChild(table);

    }

    fetch(url).then(res => res.text()).then(text => processData(text));
};