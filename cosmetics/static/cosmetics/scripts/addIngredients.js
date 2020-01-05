const addRelatedName = ingredientElement => {
  const newRelatedName = `
      <div class="form-item">
        <label for="name">Related Name:</label>
        <div class="alert">
    <div class="ingredient-name-alert">
    </div></div>
        <input type="text" name="ingredient-name">
      </div> `;

  const div = document.createElement('div');
  div.classList.add('single-ingredient-related-name-related');
  div.innerHTML = newRelatedName;
  ingredientElement.appendChild(div);
};

document
  .querySelector('input.add-related-name')
  .addEventListener('click', () => {
    addRelatedName(document.querySelector('div.single-ingredient-related-names'));
  });


const getIngredientData = () => {
  const ingredient = document.querySelector('div.single-ingredient');
  const ingredientNamesRelated = [];
  for (input of document.querySelectorAll('div.single-ingredient-name-related input')) {
    ingredientNamesRelated.push(input.value);
  }
  return ingredientData = {
    main_name: ingredient.querySelector('div.single-ingredient-name input').value,
    description: ingredient.querySelector('div.single-ingredient-description textarea').value,
    ingredient_type: ingredient.querySelector('div.single-ingredient-type select').value,
    natural: ingredient.querySelector('div.single-ingredient-natural input').checked,
    hypoallergenic: ingredient.querySelector('div.single-ingredient-hypoallergenic input').checked,
    related_names: ingredientNamesRelated,
  };
};


const checkCompability= (name,element,regex,alert) => {
  const correct=regex.test(element);
  const stringPath = 'form div.ingredient-'.concat(name).concat('-alert'); 
  const formSpace = document.querySelector(stringPath);
  if(!correct){
    formSpace.innerHTML = alert;
    return false;
  }
  formSpace.innerHTML = "";
  return true;
};

const initialValidate = () => {
  var correct=true;
  const jsonData = getIngredientData();
  const name =  jsonData['main_name'];
  var regex = /.{3,50}/;
  if(!checkCompability("name",name,regex,"Enter correct name (between 3 and 50 characters)")){
    correct = false;
  }
  const description = jsonData['description'];
  regex = /.{10,5000}/;
  if (!checkCompability("description",description,regex,"Enter correct description (between 10 and 5000 characters)")){
    correct = false;
  }
  const ingredient_type =  jsonData['ingredient_type'];
  regex = /.{10,5000}/;
  if (!checkCompability("type",ingredient_type,regex,"Choose one type")){
    correct = false;
  }
  return correct;
};

const addIngredient = async () => {
  if(initialValidate()==true){
  const jsonData = getIngredientData();
  const resp = await requestPost('/ingredient/add', jsonData);
  console.log(resp);
  window.location.replace('/success')
}
};

document
  .querySelector('form button')
  .addEventListener('click', addIngredient);
