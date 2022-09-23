import React from 'react';

type ExpandableContainerProps = {
  className?: string;
  parentNode: React.ReactNode;
  childNodes?: React.ReactNode;
  indent?: number;
  expanded?: boolean;
};

function ExpandableContainer({
  className,
  parentNode,
  childNodes,
  indent = 16,
  expanded = true,
}: ExpandableContainerProps) {
  return (
    <div className={`${className || ''}`}>
      <div className="flex items-center justify-between">{parentNode}</div>
      <div
        className={`flex flex-col ${!expanded && 'hidden'}`}
        style={{ paddingLeft: indent }}
      >
        {childNodes}
      </div>
    </div>
  );
}

export default ExpandableContainer;
