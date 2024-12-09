document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("#review-form");
    const responseBox = document.querySelector(".response-box");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        const review = form.querySelector("input[name='review']").value;

        fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ review }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    responseBox.textContent = `Error: ${data.error}`;
                } else {
                    responseBox.textContent = `Sentiment: ${data.sentiment}`;
                }
            })
            .catch((error) => {
                responseBox.textContent = "Error processing your review.";
                console.error(error);
            });
    });
});
