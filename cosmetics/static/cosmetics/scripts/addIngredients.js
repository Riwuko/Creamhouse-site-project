const addRelatedName = ingredientElement => {
  const newRelatedName = `
    <div class="single-ingredient-name">
        <label for="name">Related Name:</label>
        <input type="text" name="ingredient-name">
    </div>`;
  const div = document.createElement('div');
  div.innerHTML = newRelatedName;
  ingredientElement.parentElement.appendChild(div);
};

document
  .querySelector('input.add-related-name')
  .addEventListener('click', () => {
    addRelatedName(document.querySelector('div.single-ingredient'));
  });

const requestPost = async (url, jsonData) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': Cookies.get('csrftoken'),
    },
    body: JSON.stringify(jsonData),
    credentials: 'include',
  });
  return response.json();
};

const getIngredientNames = () => {
  const ingredientNames = [];
  for (input of document.querySelectorAll('div.single-ingredient-name input')) {
    ingredientNames.push(input.value);
  }
  return ingredientNames;
};

const addIngredient = async () => {
  const jsonData = getIngredientNames();
  const resp = await requestPost('/ingredient/add', jsonData);
  console.log(resp);
  window.location.replace('/')
};

document
  .querySelector('form button')
  .addEventListener('click', addIngredient);
