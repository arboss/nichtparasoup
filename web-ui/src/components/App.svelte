<script>
	import ImagePane from './ImagePane.svelte'	

	let images = []
	let maximum = 10
	let interval = 5000

	const nextImage = async () => {
		try {
			const newImage = await fetch('/get')
			images = [await newImage.json(), ...images]

			if(images.length > maximum) {
				images = images.slice(0,maximum)
			}
		} catch (ex) {
			// image amazing ui response here
			console.log(ex)
		}

		setTimeout(nextImage, interval)
	}

	nextImage()
</script>

<markup>
	div
		label(for=maximum-input) history length
		input#maximum-input(bind:value='{maximum}')
		label(for=interval-input) interval(ms)
		input#interval-input(bind:value='{interval}')
	ImagePane(images='{images}')
</markup>

<style>
	input {
		margin-right: 50px;
	}

	:global(html,body) {
		background-color: $background-color;
	}
</style>