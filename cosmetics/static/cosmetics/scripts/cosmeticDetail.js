const results = document.querySelector('div.content div.results');
const checkCompositionButton = results.querySelector('button');

checkCompositionButton.addEventListener('click', async () => {
  const pkRegex = /cosmetic\/show\/(\d+)/;
  const pk = pkRegex.exec(window.location.href)[1];
  const response = await requestGet(
    `/api/cosmetic/${pk}/check-composition`,
    '',
  );
  console.log(response);
  results.innerHTML = showCompositions(response);
});

const showCompositions = response => {
  const compositions = [];
  for (composition of response['ingredients']) {
    const {
      description,
      hypoallergenic,
      ingredient_type,
      natural,
      verified,
    } = composition;
    compositions.push(
      `<div>description: ${description}</div>
       <div>hypoallergenic ${hypoallergenic}</div>`,
    );
  }
  return compositions.join('<br>');
};
