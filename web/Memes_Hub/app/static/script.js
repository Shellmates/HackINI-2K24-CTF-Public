function downloadMeme(filename) {
    fetch(`/download?filename=${filename}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return "file downloaded"
});
}
