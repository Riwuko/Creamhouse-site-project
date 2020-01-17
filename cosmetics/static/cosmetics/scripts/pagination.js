const changePagination = response => {
  const paginationElementsArray = [];
  if (response['previous_page']) {
    paginationElementsArray.push(`<span class="pagination-panel"><span id="firstPage" data-page="1">&laquo; first</span></span><span class="pagination-panel"><span id="previousPage" data-page="${response['previous_page']}">previous</span></span>`)
  }
  paginationElementsArray.push(`<span class="pagination-panel-no-a"><span>Page ${response['current_page']} of ${response['last_page']}.</span></span>`);
  if (response['next_page']) {
    paginationElementsArray.push(`<span class="pagination-panel"><span id="nextPage" data-page="${response['next_page']}">next</span></span><span class="pagination-panel"><span id="lastPage" data-page="${response['last_page']}">last &raquo;</span></span>`)
  }
  document.querySelector('div.pagination span.step-links').innerHTML = paginationElementsArray.join('');

  const previousPage = document.getElementById('previousPage');
  const firstPage = document.getElementById('firstPage');
  const nextPage = document.getElementById('nextPage');
  const lastPage = document.getElementById('lastPage');
  if (previousPage) {
     previousPage.addEventListener('click', () => changeCosmeticFilters(previousPage.getAttribute('data-page')));
     firstPage.addEventListener('click', () => changeCosmeticFilters(firstPage.getAttribute('data-page')));
  }
  if (nextPage) {
    nextPage.addEventListener('click', () => changeCosmeticFilters(nextPage.getAttribute('data-page')));
    lastPage.addEventListener('click', () => changeCosmeticFilters(lastPage.getAttribute('data-page')));
  }
};
