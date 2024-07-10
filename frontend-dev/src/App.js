const API_KET = 'apiKey'

const summitButton=document.querySelector('#submit')


async function fetchData(){
  const response=await fetch("https://api.openai.com/v1/chat/completions",{
    method:"POST",
    headers:{
      Authorization:"Bearer ${API_KEY}",
      "Content-Type":"application/json"

    },
    body:JSON.stringify({
      model:"gpt-4",
      messages:[
        {
          role:"user",
          content: "Hello!"
        }]
    })
  })
  const data=await response.json()
  console.log(data)
}
async function getmessage() {
  console.log('clicked')
  try {
    
  } catch (error) {
    
  }
  
}

summitButton.addEventListener('click',getmessage)
fetchData()