#!/usr/bin/node
const BaseSquare = require('./5-square.js')

class Square extends BaseSquare
{
    charprint(c)
    {
        if (c == undefined)
        {
            c = 'X';
        }
        const row = c.repeat(this.size);
        for (let i = 0; i < this.size; i++)
        {
            console.log(row);
        }
    }
}
module.exports = Square;