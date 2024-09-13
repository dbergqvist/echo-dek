<script>
  import { onMount } from 'svelte';
  let query = '';
  let artists = [];

  async function searchArtist() {
    const response = await fetch(`/search_artist?query=${query}`);
    artists = await response.json();
  }
</script>

<main>
  <h1>Search for an Artist</h1>
  <input type="text" bind:value={query} placeholder="Enter artist name" />
  <button on:click={searchArtist}>Search</button>

  {#if artists.length > 0}
    <ul>
      {#each artists as artist}
        <li><a href={`/artist/${artist.id}`}>{artist.name}</a></li>
      {/each}
    </ul>
  {/if}
</main>