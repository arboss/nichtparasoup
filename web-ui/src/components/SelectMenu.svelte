<script>

</script>

<markup>
    <div>
        <span>text</span>
    </div>
</markup>

<style>
    div {
        padding: 11px 16px;
        display: inline-block;
        
        span {
            color: $primary-color;
            text-decoration:underline;
            text-decoration-style: dotted;
            font-size: 21px;
            font-family: 'Roboto', arial;
            line-height: 1;
        }

        &:hover {
            span {
                color: lighten($primary-color, 20%);
            }

            cursor: pointer;
        }
    }
    
</style>