# Prodlane Working Student Fullstack Challenge
## Introduction
This challenge consists of three parts - the last one is optional:
1. [Part 1](#part-1) - of the challenge is to create a simple react component that can be used to display a expandable tree of knowledges.
2. [Part 2](#part-2) - of the challenge is to create a caching class that can be used to store mails that have already been converted to data points.
3. [Part 3](#part-3) (**optional**) - of the challenge is to create an algorithm that can be used to create a tree of knowledges based on a flat map of knowledges.

We track the time you need to solve the tasks. The time starts with the invitation to the Github repo and ends with the timestamp of your last commit. 
How long you need to solve the tasks plays a role in the evaluation, but is **not** the most important point. It is **more** important to implement clean, working and performant solutions.

## Part 1
In ([input-task-1.json](./task-1/input-task-1.json)) you will find some example data for an abridged version of a data structure we use in production. Your task is to create a component that takes this example data as one of its props. The component should then display a menu tree showing each of the knowledge object's titles. Each level of the menu tree shall be individually expandable and collapsable. You can create as many components to achieve this as you see fit.
We already set up a react app so you can start coding right away. All you have to to is ```yarn install``` and then use ```yarn dev```to start the app.

The tasks must be solved in React and Typescript (alternatively JS).

## Part 2

The mail fetcher service periodically fetches mail from any mail server, converts the mails to data points and stores them in a database.

Due to the nature of the smtp protocol used to retrieve mail, only a date filter and not a datetime filter can be used when retrieving mail. The mail fetcher service must therefore fetch all mails from at least the last day.

To ensure that we do not convert mail to data points more than once, we want to create a **caching class** that stores the combination of the *mail-account-id*, the *message-id* of the converted mail and the *datetime* at which the mail was converted.

The tasks should **preferably** be solved in Python or Golang. If you do not have enough experience in one of these two languages, any other language can be used.

### Requirements
- When initializing the cache, all mails already converted to data points are to be loaded from the database into the cache. (Use dummy function for this)
- Function to add new mails to the cache. (by mail-account-id + message-id + datetime)
- Function to check if a mail is already in the cache. (by message-id)
- Function to remove mails from the cache that are older than a certain age. (by datetime)
- Function that returns the datetime of the oldest mail in the cache.

## Part 3
**This part is optional**. The given input ([input-task-3.json](./task-3/input-task-3.json)) is a flat map of knowledges. From this, a tree structure, as used as input in the first part of the challenge, is to be generated. 
Thus, every knowledge shall be a node in the tree. The root nodes are the knowledges with the lowest level (no parent). The children of a node are linked to the node by the parent property. The algorithm must run in **0(n)** time and must work for any depth of the tree.

The tasks should **preferably** be solved in Python or Golang or Typescript. If you do not have enough experience in one of these languages, any other language can be used.