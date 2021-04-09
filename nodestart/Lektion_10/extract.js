exports.extract = (alexa) => {
    const intent = alexa.request.intent;
    return intent.slots.Item.value;
}