<script>
import { onMount } from "svelte";
import { Tetris } from '$lib/klasser.js'

const ENHET = 40
const BREDDE = 10*ENHET
const HØYDE = 22*ENHET


let canvas
let ctx
let interval

let spillbrett = new Tetris(BREDDE, HØYDE)

onMount(() => {
    ctx = canvas.getContext('2d')
    interval = setInterval(() => update(ctx), 1000)
})

function update(ctx) {
    ctx.fillStyle = 'black'
    ctx.fillRect(0, 0, 1000, 1000)
}
</script>

<div class="window">
    <canvas bind:this={canvas} height={spillbrett.høyde}px width={spillbrett.bredde}px/>
</div>

<style>
    .window {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
    }
</style>