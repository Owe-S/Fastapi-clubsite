// generate-swagger.js
const swaggerJSDoc = require('swagger-jsdoc');
const fs           = require('fs');
const path         = require('path');

// 1) Define your OpenAPI metadata
const swaggerDefinition = {
  openapi: '3.0.0',
  info: {
    title: 'ClubSite CMS API',
    version: '1.0.0',
    description: 'Automatically generated OpenAPI spec for ClubSite CMS'
  },
  servers: [
    { url: 'https://api.clubsitecms.no/v1', description: 'Production' },
    { url: 'http://localhost:8000/v1',      description: 'Local Dev' }
  ]
};

// 2) Point at your JSDoc-annotated files:
const options = {
  swaggerDefinition,
  apis: ['./routes/**/*.js', './models/**/*.js'], 
};

// 3) Generate and write out the JSON
const swaggerSpec = swaggerJSDoc(options);
const outPath     = path.join(__dirname, 'docs', 'swagger.json');
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(swaggerSpec, null, 2));

console.log(`✅  Generated swagger.json at ${outPath}`);
