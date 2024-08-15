<script>
    import { onMount } from "svelte";
    
    const WIDTH = 1300
    const HEIGHT = 700
    
    class Cannon {
        constructor() {
            this.x = 160
            this.y = HEIGHT / 2 - 20
            this.width = 50
            this.height = 15
            this.angle = 0
            this.pivotX = this.x + 7
            this.pivotY = this.y + this.height/2
            this.mouthX = this.x + this.width
            this.mouthY = this.y + this.height/2
        }

        setAngle(angle) {
            this.angle = angle * Math.PI / 180
        }
    }

    let cannon = new Cannon()
    
    let canvas
    let ctx
    let interval
    
    onMount(() => {
        ctx = canvas.getContext('2d')
        interval = setInterval(() => update(ctx), 100)
    })
    
    function update(ctx) {
        /* Background */
        ctx.fillStyle = '#c3edec'
        ctx.fillRect(0, 0, WIDTH, HEIGHT)
        /* Ocean */
        ctx.fillStyle = '#437dbc'
        ctx.fillRect(0, HEIGHT - 150, WIDTH, 150)
        /* Fort */
        ctx.fillStyle = '#b4b0ae'
        ctx.fillRect(0, HEIGHT/2, 200, HEIGHT/2)
        ctx.fillRect(0, HEIGHT/2 - 30, 50, 50)
        ctx.fillRect(100, HEIGHT/2 - 30, 50, 50)
        /* Cannon */
        ctx.save()
        ctx.translate(cannon.pivotX, cannon.pivotY)
        ctx.rotate(- cannon.angle * Math.PI/180)
        ctx.fillStyle = '#283746'
        ctx.fillRect(cannon.x - cannon.pivotX, cannon.y - cannon.pivotY, cannon.width, cannon.height)
        ctx.restore()
        ctx.fillStyle = '#4b3b34'
        ctx.fillRect(150, HEIGHT / 2 - 15, 50, 15)
        
    }
    </script>
    
    <div class="window">
        <canvas bind:this={canvas} height={HEIGHT}px width={WIDTH}px/>
        <div class="infoPanel">
            <label for="">Vinkel: </label><input type="number" bind:value={cannon.angle} min=0 max=90>
        </div>
    </div>
    
    
    <style>
        .window {
            display: flex;
            flex-direction: column;
            row-gap: 30px;
            align-items: center;
            justify-content: center;
            height: 100vh;
            width: 100vw;
        }
    </style>