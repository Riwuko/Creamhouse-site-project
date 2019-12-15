const chooseIngredientType = document.querySelector('select.ingredients-filters-types');
const chooseIngredientNatural = document.querySelector('input.ingredients-filters-natural');
const chooseIngredientHypoallergenic = document.querySelector('input.ingredients-filters-hypoallergenic');
const formSpace = document.querySelector('form div.ingredients-chosen-filters');
const changeFormTemplate = () => {
  const ingredientType = chooseIngredientType.value;
  const ingredientNatural = chooseIngredientNatural.checked;
  const ingredientHypoallergenic = chooseIngredientHypoallergenic.checked;
  
  changeIngredientsFilters();

  console.log(ingredientType, ingredientNatural, ingredientHypoallergenic);
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

const changeIngredientsFilters = async () => {
  const jsonData = getIngredientsFiltersData();
  console.log(jsonData);
  // resp = await requestPost('/cosmetic/add', jsonData);
  // console.log(resp);
};


