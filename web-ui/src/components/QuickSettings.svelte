<script>
    import { fly } from 'svelte/transition'
    import SelectMenu from './SelectMenu.svelte'

    export let interval = 5000
    export let historyLength = 10
    
    let visible = false
    let hideDelayTimeout = -1
    
    const historyLengthOptions = [1, 20, 50, 100]
    
    const show = () => {
        clearTimeout(hideDelayTimeout)
        visible = true
    }
    
    const hide = () => {
        clearTimeout(hideDelayTimeout)
        hideDelayTimeout = setTimeout(() => {
            visible = false
        }, 500)
    }

    $: console.log(visible)
</script>

<markup>
    #quick-settings-bar(on:mouseover='{show}')
        +if ('true')
            #quick-settings-controls(on:mouseout='{hide}' transition:fly="{{ y: 50, duration: 500 }}")
                //- label(for=interval-input) interval(ms)
                //- input#interval-input(bind:value='{interval}')
                //- label(for=history-length-input) historyLength(ms)
                //- input#history-length-input(bind:value='{historyLength}')
                SelectMenu
</markup>

<style>
    #quick-settings-bar {
        height: $quick-settings-bar-height;

        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        
        #quick-settings-controls {
            height: 100%;
            background-color: $highlight-color;
        }
    }
</style>