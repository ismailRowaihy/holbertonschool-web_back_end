export default function handleResponseFromAPI(promise){
    promise.then((data) =>{
        return {
            "status":200,
            "body":'success'
        }
    }).catch((data) =>{
        return new Error()
    })
    console.log('Got a response from the API')
}