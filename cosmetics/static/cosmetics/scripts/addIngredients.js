const addRelatedName = ingredientElement => {
  const newRelatedName = `
        <label for="name">Related Name:</label>
        <input type="text" name="ingredient-name">`;
  const div = document.createElement('div');
  div.classList.add('single-ingredient-name-related');
  div.innerHTML = newRelatedName;
  ingredientElement.appendChild(div);
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

const getIngredientData = () => {
  const ingredient = document.querySelector('div.single-ingredient');
  const ingredientNamesRelated = [];
  for (input of document.querySelectorAll('div.single-ingredient-name-related input')) {
    ingredientNamesRelated.push(input.value);
  }
  return ingredientData = {
    main_name: ingredient.querySelector('div.single-ingredient-name input').value,
    description: ingredient.querySelector('div.single-ingredient-description textarea').value,
    ingredient_type: ingredient.querySelector('div.single-ingredient-type input').value,
    natural: ingredient.querySelector('div.single-ingredient-natural input').checked,
    hypoallergenic: ingredient.querySelector('div.single-ingredient-hypoallergenic input').checked,
    related_names: ingredientNamesRelated,
  };
};

const addIngredient = async () => {
  const jsonData = getIngredientData();
  const resp = await requestPost('/ingredient/add', jsonData);
  console.log(resp);
  window.location.replace('/')
};

document
  .querySelector('form button')
  .addEventListener('click', addIngredient);
