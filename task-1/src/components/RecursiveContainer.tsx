import React, { useState } from 'react';
import ExpandableContainer from "./ExpandableContainer"

function RecursiveContainer(props : any) : any {
    
    const [expanded, setExpanded] = useState(true)
    
    return <div onClick={(e) => {
        e.stopPropagation();
        setExpanded(!expanded)
    }} >
        <ExpandableContainer  parentNode ={props.data.title} expanded={expanded} childNodes ={
        
        props.data.child_knowledge.map((item:any) => (
            <RecursiveContainer data ={item}></RecursiveContainer>
        ))
    }
 ></ExpandableContainer>
    </div>
}

export default RecursiveContainer;
