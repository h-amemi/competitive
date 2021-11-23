"use strict";

const main = arg => {
    const inputs = arg.trim().split("\n");

    const N = parseInt(inputs[0])

    const X = inputs[1].split(" ").map(Number);
    const M = parseInt(inputs[2]);
    const sousas = inputs[3].split(" ").map(Number);

    sousas.forEach(koma => {
        const masu = X[koma - 1];
        const dup = X.indexOf(masu + 1);
        if ((masu !== 2019) && (dup == -1)) {
            X[koma - 1] = masu + 1;
        }
    });

    X.forEach(masu => {
        console.log(masu)
    });
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'))
