import React from 'react';
import ExpandableContainer from "./ExpandableContainer"

function RecursiveContainer(props : any) : any {
    
    
    return <ExpandableContainer parentNode ={props.data.title} expanded={false} childNodes ={
        
            props.data.child_knowledge.map((item:any) => (
                <RecursiveContainer data ={item}></RecursiveContainer>
            ))
        }
     ></ExpandableContainer>
}

export default RecursiveContainer;
