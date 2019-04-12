$(function() {
   
    $('#generate').click(() => {
        let keywords = "query=" + $('#keywords').val().replace(/[, ]+/g, "%20") + "&";
        console.log(keywords);
        localStorage.setItem('keywords', keywords)
    });
});