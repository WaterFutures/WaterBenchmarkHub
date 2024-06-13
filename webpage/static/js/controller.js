"use strict";

window.onload = () => {
    new Database().getDatabase().then(database => {
        var myBenchmarks = []
        for (var [key, value] of Object.entries(database.resources)) {
            value["id"] = key;
            myBenchmarks.push(value);
        }

        new Vue({
            el: "#app",
            components: {
                benchmark: {
                    props: ["benchmark"],
                    template: `
                    <b-list-group-item :href="benchmark.permalink">
                      <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">{{benchmark.name}}</h5>
                        <small>{{benchmark.year}}</small>
                      </div>
                      <p class="mb-1">
                        {{benchmark.desc}}
                      </p>
                    </b-list-group-item>
                    `
                },
                searchterm: {
                    props: ["text"],
                    template: `
                    <b-button pill variant="primary" @click="() => $emit('click-on-close')">
                        "{{text}}" <b-icon icon="x-circle-fill"></b-icon>
                    </b-button>
                    `
                }
            },
            data: {
                allTags: database.tags,
                activeTags: [],
                searchText: "",
                allSearchTexts: [],
                allBenchmarks: myBenchmarks,
                benchmarks: myBenchmarks
            },
            methods: {
                onClickOnTag(tagId) {
                    if(this.activeTags.includes(tagId)) {
                        this.activeTags.splice(this.activeTags.indexOf(tagId), 1);
                    }
                    else {
                        this.activeTags.push(tagId);
                    }

                    this.filterBenchmarks();
                },
                onRemoveSearchText(searchText) {
                    this.allSearchTexts.splice(this.allSearchTexts.indexOf(searchText), 1);
                    
                    this.filterBenchmarks();
                },
                onClickSearch() {
                    if(this.searchText != "") {
                        this.allSearchTexts.push(this.searchText);
                        this.searchText = "";
    
                        this.filterBenchmarks()
                    }
                },
                filterBenchmarks() {
                    var benchmarks = this.allBenchmarks;

                    if(this.activeTags.length != 0) {
                        // Filter by tags
                        benchmarks = benchmarks.filter((b) => {
                            return this.activeTags.some((t) => b.tags.includes(t));
                        });
                    }
                    if(this.allSearchTexts.length != 0) {
                        // Filter by search texts
                        for(var i=0; i != this.allSearchTexts.length; i++) {
                            var searchKeywords = this.allSearchTexts[i].split(" ");

                            benchmarks = benchmarks.filter((b) => searchKeywords.some((k) => {
                                var _k = k.toLowerCase();
                                return b.tags.some(item => item.toLowerCase().includes(_k))|
                                    b.keywords.some(item => item.toLowerCase().includes(_k)) |
                                    b.name.toLowerCase().includes(_k) |
                                    b.desc.toLowerCase().includes(_k);
                            }));
                        }
                    }

                    this.benchmarks = benchmarks
                }
            }
          });
    });
}