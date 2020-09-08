<script>
    import ImageItem from './ImageItem.svelte'

    export let images

    $: console.log(images)
</script>

<markup>
    +each('images as image')
        ImageItem(url='{image.uri}' alt='alt')
</markup>

<style>

</style>