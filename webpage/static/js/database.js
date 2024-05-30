"use strict";


class Database {
    getDatabase(rootDir="") {
        return new Promise(resolve => {
            fetch(`${rootDir}static/database.json`, {
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
