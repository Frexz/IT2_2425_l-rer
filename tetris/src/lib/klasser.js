export class Tetris {
    constructor(bredde, høyde) {
        this.bredde = bredde
        this.høyde = høyde
        this.brett = this.byggBrett()
    }

    byggBrett() {
        let brett = []
        for (let i = 0; i < 22; i++) {
            brett.push([])
            for (let j = 0; j < 10; j++) {
                brett[i].push(0)
            }
        }

        return brett
    }
}

class Node {
    constructor(x, y) {
        this.x = x
        this.y = y
        this.up
        this.down
        this.left
        this.right
    }
}

class Figur {
    constructor() {

    }

    flytt() {}
    roter() {}
}