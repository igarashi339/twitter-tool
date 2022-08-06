import { createTheme } from '@mui/material/styles';

let theme = createTheme({})

theme = createTheme({
  components: {
    MuiToolbar: {
      styleOverrides: {
        root: {
          // paddingLeft: '16px',
          // paddingRight: '16px',
          [theme.breakpoints.up('sm')]: {
            paddingLeft: '16px',
            paddingRight: '16px',
          }
        }
      }
    }
  },
  mixins: {
    toolbar: {
      minHeight: '64px',
    }
  }
});

export default theme;