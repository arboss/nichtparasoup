<script>
    import ImageItem from './ImageItem.svelte'
    import { blur } from 'svelte/transition'

    export let images

    $: console.log(images)
</script>

<markup>
    +each('images as image (image.id)')
        span(transition:blur)
            ImageItem(url='{image.uri}', alt='alt')
</markup>

<style>

</style>