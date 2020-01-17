const chooseIngredientType = document.querySelector('select.ingredients-filters-types');
const chooseIngredientNatural = document.querySelector('input.ingredients-filters-natural');
const chooseIngredientHypoallergenic = document.querySelector('input.ingredients-filters-hypoallergenic');
const formSpace = document.querySelector('form div.ingredients-chosen-filters');
const changeFormTemplate = () => {
  const ingredientType = chooseIngredientType.value;
  const ingredientNatural = chooseIngredientNatural.checked;
  const ingredientHypoallergenic = chooseIngredientHypoallergenic.checked;

};
chooseIngredientType.addEventListener('change', changeFormTemplate);
chooseIngredientNatural.addEventListener('change',changeFormTemplate);
chooseIngredientHypoallergenic.addEventListener('change',changeFormTemplate);


const getIngredientsFiltersData = () => {
	const ingredientType = chooseIngredientType.value;
 	const ingredientNatural = chooseIngredientNatural.checked;
  	const ingredientHypoallergenic = chooseIngredientHypoallergenic.checked;
	return IngredientsData = {
    	ingredient_type: ingredientType,
    	natural: ingredientNatural,
    	hypoallergenic: ingredientHypoallergenic,
  	}
};

const showFilteredIngredients = response => {
  ingredientsArray = [];
  const {ingredients} = response;
  for (ingredientPk in ingredients) {
    ingredientsArray.push(`<li><a href="/ingredient/show/${ingredientPk}">${ingredients[ingredientPk]}</a></li>`)
  }
  return ingredientsArray.join('');
};

const changeIngredientsFilters = async pageNumber  => {
  const jsonData = {ingredientFilterData: getIngredientsFiltersData(), page:pageNumber};
  console.log(jsonData);
  const url = '/ingredient/filter';
  const response = await requestPost(url, jsonData);
  const filteredIngredients = showFilteredIngredients(response);
  const ingredientsList = document.querySelector('ul');
  changePagination(response);
  ingredientsList.innerHTML = filteredIngredients;
};

const filterButton = document.querySelector('form button');
filterButton.addEventListener('click', () => changeIngredientsFilters(1));





