<script context="module">
  export async function load({ params }) {
    const response = await fetch(`/album/${params.id}/uris`);
    const uris = await response.json();
    return { props: { uris } };
  }
</script>

<script>
  export let uris;
</script>

<main>
  <h1>Album URIs</h1>
  <p>Spotify: <a href={uris.spotify_uri}>{uris.spotify_uri}</a></p>
  <p>Apple Music: <a href={uris.apple_music_uri}>{uris.apple_music_uri}</a></p>
</main>