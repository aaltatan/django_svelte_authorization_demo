<script>
  import { onMount } from 'svelte';
  import { location, pop } from 'svelte-spa-router';

  onMount(() => {
    let timeout = setTimeout(() => {
      pop();
    }, 3000)
    return () => {
      clearTimeout(timeout);
    }
  })

</script>

<div>
  not found page {$location}
</div>