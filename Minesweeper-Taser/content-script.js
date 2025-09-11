// content-script.js
(() => {
    'use strict';

    const elementSelector = '#face';
    const lostClassName = 'facedead';

    const targetElement = document.querySelector(elementSelector);

    if (targetElement) {
        const observer = new MutationObserver(mutations => {
            mutations.forEach(mutation => {
                if (mutation.attributeName === 'class' && targetElement.classList.contains(lostClassName)) {
                    fetch('http://localhost:8080/')
                        .then(response => response.text())
                        .then(data => {
                            console.log("Response from server:", data);
                        })
                        .catch(error => {
                            console.error("Error:", error);
                        });
                    console.log('Lost!');
                    document.body.style.backgroundColor = "red";
                } else {
                    document.body.style.backgroundColor = "";
                }
            });
        });

        observer.observe(targetElement, {
            attributes: true,
            childList: false,
            subtree: false
        });
    }
})();
