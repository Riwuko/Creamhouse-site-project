const results = document.querySelector('div.results');
const checkCompositionButton = results.querySelector('button');

checkCompositionButton.addEventListener('click', async () => {
  const pkRegex = /cosmetic\/show\/(\d+)/;
  const pk = pkRegex.exec(window.location.href)[1];
  const response = await requestGet(
    `/api/cosmetic/${pk}/check-composition`,
    '',
  );
  results.innerHTML = showCompositions(response);
});

const showCompositions = response => {
  const compositions = [];
  compositions.push(
      `<br>
      <div class="custom-h1">Cosmetic composition</div>
      <div class="composition-table">
       <table>
        <tr>
       <th><div class="composition-table-header">Name</div></th>
       <th><div class="composition-table-header">Ingredient type</div></th>
       <th><div class="composition-table-header">Natural</div></th>
       <th><div class="composition-table-header">Hypoallergenic</div></th>
       <th><div class="composition-table-header">Verified</div></th>
       <th><div class="composition-table-header">Description</div></th>
       </tr>
       <tr>
       `);
  console.log(response['ingredients']);
  for (composition of response['ingredients']) {
    const {
      ingredient_names,
      description,
      hypoallergenic,
      ingredient_type,
      natural,
      verified,
    } = composition;
compositions.push(
      `
      <th>
       `);
    for (name of ingredient_names){
      compositions.push(
      `
       ${name}<br>
       `);
    }

        compositions.push(
      `
      </th>
       `);

    compositions.push(`
        <th> ${ingredient_type}</th>
        <th>${natural}</th>
        <th>${hypoallergenic}</th>
        <th>${verified}</th>
        <th>${description}</th>
        </tr>
       `, 
    );
  }
      compositions.push(
      `
      </table>
      </div>
       `);
  return compositions.join('');
};
