<script>
    export let url
    export let alt
</script>

<markup>
    img(src='{url}' alt='{alt}')
</markup>

<style>
    img {
        border: 1px solid $primary-color;
        margin: 0 5px 5px 0;
    }
</style>