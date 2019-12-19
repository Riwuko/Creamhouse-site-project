const requestGet = async (url, querystring) => {
  const response = await fetch(`${url}?${querystring}`, {
    method: 'GET',
    credentials: 'include',
  });
  return response.json();
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