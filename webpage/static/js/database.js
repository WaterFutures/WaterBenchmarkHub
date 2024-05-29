"use strict";


class Database {
    getDatabase() {
        return new Promise(resolve => {
            fetch("../static/database.json", {
                method: "GET"
            })
            .then(r => r.json())
            .then(r => resolve(r))
            .catch((error) => {
                console.error(error);
                resolve(undefined);
            })
        });
    }
}
