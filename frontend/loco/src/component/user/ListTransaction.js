import React, { useEffect } from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import axios from 'axios';
import Autocomplete from '@material-ui/lab/Autocomplete';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles((theme) => ({
    table: {
        maxWidth: 800,
        margin: 'auto'
    },
    root: {
        '& > *': {
            margin: theme.spacing(1),
            width: '25ch',
        },
    },
    head: {
        backgroundColor: theme.palette.common.black,
        color: 'white',
    },
}));


export default function AlertDialog() {
    const [open, setOpen] = React.useState(false);
    const [data, setData] = React.useState([])
    const [currency, setCurrency] = React.useState(10);
    const classes = useStyles();

    const handleChange = (event) => {
        setCurrency(event.target.value);
    };

    const handleClickOpen = () => {
        setOpen(true);
    };


    useEffect(() => {
        axios('http://127.0.0.1:8000/transactionservice/transaction/20')
            .then(response => {
                setData(response.data);
                console.log(response.data)
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
            })
    }, [])

    useEffect(() => {
        axios('http://127.0.0.1:8000/transactionservice/transaction/parents_list')
            .then(response => {
                setCurrency(response.data);
                console.log(response.data)
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
            })
    }, [])

    const handleClose = () => {
        setOpen(false);
    };

    return (
        <div>
            <Grid container spacing={1}>
                <Grid item container xs={12} spacing={3} justifyContent="center"
                    alignItems="center">
                    <Autocomplete
                        id="combo-box-demo"
                        options={data}
                        size="small"
                        getOptionLabel={(option) => option.type}
                        style={{ width: 170, margin: 'auto' }}
                        renderInput={(params) => <TextField {...params} label="Select Type" variant="outlined" />}
                    />
                    <Autocomplete
                        id="combo-box-demo"
                        options={currency}
                        size="small"
                        getOptionLabel={(option) => option.parent_id}
                        style={{ width: 170, margin: 'auto' }}
                        renderInput={(params) => <TextField {...params} label="Select Parent" variant="outlined" />}
                    />
                    <Button variant="outlined" color="primary" onClick={handleClickOpen}>
                        Add Transaction
                    </Button>
                </Grid>
            </Grid>
            <TableContainer style={{ marginTop: '100px'}}>
                <Table className={classes.table} size="small" aria-label="a dense table">
                    <TableHead className={classes.head}>
                        <TableRow>
                            <TableCell style={{ color: 'white' }}>Index</TableCell>
                            <TableCell style={{ color: 'white' }} align="left">Amount</TableCell>
                            <TableCell style={{ color: 'white' }} >Type</TableCell>
                            <TableCell style={{ color: 'white' }} >Parent Id</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {data.map((d, index) => (
                            <TableRow key={index}>
                                <TableCell component="th" scope="row">
                                    {index + 1}
                                </TableCell>
                                <TableCell>{d.amount}</TableCell>
                                <TableCell>{d.type}</TableCell>
                                <TableCell >{d.parent_id}</TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>

            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
            >
                <DialogTitle id="alert-dialog-title">{"Add New Transaction "}</DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        Please Enter the Required Details :
                    </DialogContentText>
                    <form className={classes.root} noValidate autoComplete="off">
                        <TextField
                            id="standard-select-currency"
                            label="₹ (in Rupess)"
                            type="Number"
                            onChange={handleChange}
                            helperText="Please type your amount"
                        />
                        <TextField id="outlined-basic" label="Type" variant="outlined" />
                        <TextField
                            id="standard-select-currency"
                            label="Parent Id"
                            type="Number"
                            onChange={handleChange}
                            helperText="Please enter the Parent Id"
                        />
                    </form>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="secondary">
                        Cancel
                    </Button>
                    <Button onClick={handleClose} color="primary" autoFocus>
                        Submit
                    </Button>
                </DialogActions>
            </Dialog>
        </div >
    );
}
