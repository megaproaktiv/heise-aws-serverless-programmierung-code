const extract = require('./extract')


exports.handler = async (event) => {
    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify(event.key1),
    };
    
    console.log(extract.extract(event))
    
    return response;
};
