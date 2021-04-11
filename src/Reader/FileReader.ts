import {Reader} from "./Reader";
import {readFileSync} from 'fs';

export class FileReader implements Reader {
    read(): Array<Array<number>> {
        let string = readFileSync('src/matrix.txt', "utf8");
        return string.split('\n')
            .map(str => str.split(' ')
            .map(el => Number.parseFloat(el)));
    }

}