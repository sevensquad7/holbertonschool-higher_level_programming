#!/usr/bin/node
const axios = require('axios');
let count = 0;
axios.get(process.argv[2])
  .then(res => {
    const films = res.data.results ? res.data.results : [];
    const size = films.length;
    for (let i = 0; i < size; i++) {
      films[i].characters.forEach(chr => {
        if (chr.includes('18')) count++;
      });
    }
    console.log(count);
  })
  .catch(err => {
    console.log('Error:', err);
  });
