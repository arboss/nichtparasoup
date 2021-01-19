<script>
	// external css
	import '../../node_modules/typeface-roboto/index.css'
	
	import ImagePane from './ImagePane.svelte'	
	import QuickSettings from './QuickSettings.svelte'

	let images = []
	let servedCount = 0
	let historyLength = 10
	let interval = 5000

	const nextImage = async () => {
		try {
			const response = await fetch('/get')
			let newImage = await response.json()
			
			newImage.id = servedCount
			servedCount += 1
			
			images = [newImage, ...images]

			if(images.length > historyLength) {
				images = images.slice(0,historyLength)
			}
		} catch (ex) {
			// TODO image amazing ui response here
			console.log(ex)
		}

		setTimeout(nextImage, interval)
	}

	nextImage()
</script>

<markup>
	QuickSettings(bind:interval='{interval}' bind:historyLength='{historyLength}')
	ImagePane(images='{images}')
</markup>

<style>
	:global(html,body) {
		margin: 0;
		padding: 0;
		background-color: $background-color;
	}
</style>