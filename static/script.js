const searchInput = document.getElementById('search-input');

searchInput.addEventListener('input', () => {

    query = searchInput.value;

    if (query === '') {
        spinner.style.visibility = 'hidden'
        const resultsContainer = document.querySelector('.results');
        resultsContainer.innerHTML = '';
    }

    else {
        search(query, 10)
    }

});


function search(query, max_results) {
    if (query != undefined && max_results != undefined) {

        spinner = document.getElementById('spin')
        spinner.style.visibility = 'visible'

        fetch(`/search?q=${query}&max_results=${max_results}`)
            .then(response => response.json())
            .then(response => {
                
                if (query === document.getElementById('search-input').value) {
                    const resultsContainer = document.querySelector('.results');
                    resultsContainer.innerHTML = ''; 
                    const results = response['results'];
                    results.forEach(result => {
                        const resultDiv = document.createElement('div');
                        resultDiv.classList.add('result-item');
                        resultDiv.textContent = result['data'];
                        resultDiv.addEventListener('click', () => {
                            getinfo(result['id']);
                        });
                        resultsContainer.appendChild(resultDiv); 
                    });
                    spinner.style.visibility = 'hidden'
                }
                spinner.style.visibility = 'hidden'

            }).catch(error => {
                console.error(error)
            });
    }
    else {
        throw new Error('query and max_results cannot be undefined')
    }
}

function getinfo(id){
    location.href = `/getinfo?id=${id}`
}
