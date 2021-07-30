import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import axios from 'axios';

import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { default as MatCard } from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import IconButton from '@material-ui/core/IconButton';
import EditIcon from '@material-ui/icons/Edit';
import DeleteIcon from '@material-ui/icons/Delete';
import SaveIcon from '@material-ui/icons/Save';

const Container = styled.div``;

const AddTaskCard = styled(MatCard)`
    width: 300px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    text-align: center;

    & .textfield-add-task {
        margin: 0 0 10px 0;
    }
`;

const CardsContainer = styled.div`
    margin: 20px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
`;

const TaskCard = styled(MatCard)`
    width: 300px;
    margin: 10px;

    & > .taskfield-taskcard {
        margin: 10px;
        width: calc(100% - 20px);
    }

    & > div > .taskfield-taskcard {
        width: 100%;
    }
`;

const apiBaseUrl = 'http://localhost:3030/api';

const HomePage = (): React.ReactElement => {
    const [textFieldAddTaskTitle, setTextFieldAddTaskTitle] = useState('');
    const [textFieldAddTaskContent, setTextFieldAddTaskContent] = useState('');
    const [textFieldEditTaskTitle, setTextFieldEditTaskTitle] = useState('');
    const [textFieldEditTaskContent, setTextFieldEditTaskContent] = useState('');
    const [taskData, setTaskData] = useState([]);

    const getTasks = async () => {
        return await axios.get(apiBaseUrl + '/task');
    };
    const addTask = async (title: string, content: string) => {
        return await axios({
            method: 'post',
            url: apiBaseUrl + '/task',
            data: {
                title,
                content,
            },
        });
    };
    const editTask = async (id: number, title: string, content: string) => {
        return await axios({
            method: 'post',
            url: apiBaseUrl + '/task/' + id + '/edit',
            data: {
                title,
                content,
            },
        });
    };
    const deleteTask = async (id: number) => {
        return await axios.post(apiBaseUrl + '/task/' + id + '/delete');
    };

    const transformTaskData = (tasks: any, editId = 0) => {
        const transformedTasks = tasks.map((task: any) => ({
            ...task,
            isEdit: task.id === editId ? true : false,
        }));
        return transformedTasks;
    };
    const refetchTaskData = () => {
        getTasks().then(({ data }) => {
            setTaskData(transformTaskData(data));
        });
    };

    const handleTextFieldAddTaskTitle = (event: any) => {
        setTextFieldAddTaskTitle(event.target.value);
    };
    const handleTextFieldAddTaskContent = (event: any) => {
        setTextFieldAddTaskContent(event.target.value);
    };
    const handleTextFieldEditTaskTitle = (event: any) => {
        setTextFieldEditTaskTitle(event.target.value);
    };
    const handleTextFieldEditTaskContent = (event: any) => {
        setTextFieldEditTaskContent(event.target.value);
    };
    const handleAddTask = () => {
        addTask(textFieldAddTaskTitle, textFieldAddTaskContent).then(({ status }) => {
            console.log(status);
            if (status === 201) {
                refetchTaskData();
                setTextFieldAddTaskTitle('');
                setTextFieldAddTaskContent('');
            }
        });
    };
    const handleDeleteTask = (id: number) => {
        deleteTask(id).then(({ status }) => {
            console.log(status);
            if (status === 201) {
                refetchTaskData();
            }
        });
    };
    const handleEditTask = (id: number, title: string, content: string) => {
        const tasks = [...taskData];
        setTaskData(transformTaskData(tasks, id));
        setTextFieldEditTaskTitle(title);
        setTextFieldEditTaskContent(content);
    };
    const handleSaveTask = (id: number) => {
        editTask(id, textFieldEditTaskTitle, textFieldEditTaskContent).then(({ status }) => {
            console.log(status);
            if (status === 201) {
                refetchTaskData();
            }
        });
    };

    useEffect(() => {
        refetchTaskData();
    }, []);

    return (
        <Container>
            <AddTaskCard>
                <Typography variant="subtitle1">Add Todo</Typography>
                <TextField
                    id="textfield-add-task-title"
                    className="textfield-add-task"
                    name="Add Todo Title"
                    label="Title"
                    value={textFieldAddTaskTitle}
                    onChange={handleTextFieldAddTaskTitle}
                />
                <TextField
                    id="textfield-add-task-content"
                    className="textfield-add-task"
                    name="Add Todo Content"
                    label="Content"
                    value={textFieldAddTaskContent}
                    onChange={handleTextFieldAddTaskContent}
                    multiline
                />
                <Button variant="contained" color="primary" onClick={handleAddTask}>
                    Add
                </Button>
            </AddTaskCard>
            <CardsContainer>
                {taskData.map(({ id, title, content, isEdit }) => (
                    <TaskCard key={id}>
                        {isEdit ? (
                            <TextField
                                className="taskfield-taskcard"
                                label="Title"
                                value={textFieldEditTaskTitle}
                                onChange={handleTextFieldEditTaskTitle}
                            />
                        ) : (
                            <CardHeader
                                title={title}
                                action={
                                    <IconButton onClick={() => handleEditTask(id, title, content)}>
                                        <EditIcon />
                                    </IconButton>
                                }
                            />
                        )}
                        <CardContent>
                            {isEdit ? (
                                <TextField
                                    className="taskfield-taskcard"
                                    label="Content"
                                    value={textFieldEditTaskContent}
                                    onChange={handleTextFieldEditTaskContent}
                                    multiline
                                />
                            ) : (
                                <Typography variant="body1">{content}</Typography>
                            )}
                        </CardContent>
                        <CardActions>
                            <IconButton onClick={() => handleDeleteTask(id)}>
                                <DeleteIcon />
                            </IconButton>
                            {isEdit && (
                                <IconButton onClick={() => handleSaveTask(id)}>
                                    <SaveIcon />
                                </IconButton>
                            )}
                        </CardActions>
                    </TaskCard>
                ))}
            </CardsContainer>
        </Container>
    );
};

export default HomePage;
