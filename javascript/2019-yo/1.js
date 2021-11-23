"use strict";

const main = arg => {
    const input = arg.trim();

    const A = parseInt(input.split(" ")[0]);
    const B = parseInt(input.split(" ")[1]);
    const C = parseInt(input.split(" ")[2]);

    const weeks = Math.floor(C / ((7 * A) + B));
    const amari = C % ((7 * A) + B)
    const days = Math.ceil(amari / A)
    console.log((7 * weeks) + days)
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'))
