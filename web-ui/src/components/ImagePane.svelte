<script>
    import ImageItem from './ImageItem.svelte'
    import { blur } from 'svelte/transition'

    export let images

    $: console.log(images)
</script>

<markup>
    #image-pane
        +each('images as image (image.id)')
            span(transition:blur)
                ImageItem(url='{image.uri}', alt='alt')
</markup>

<style>
    #image-pane {
        margin-top: 100px;
    }
</style>