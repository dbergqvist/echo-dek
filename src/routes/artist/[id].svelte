<script context="module">
  export async function load({ params }) {
    const response = await fetch(`/artist/${params.id}/albums`);
    const albums = await response.json();
    return { props: { albums } };
  }
</script>

<script>
  export let albums;
</script>

<main>
  <h1>Albums</h1>
  <ul>
    {#each albums as album}
      <li><a href={`/album/${album.id}`}>{album.title}</a></li>
    {/each}
  </ul>
</main>