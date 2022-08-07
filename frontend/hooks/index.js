import { useMediaQuery } from '@mui/material'

export const useLayout = () => {
  return useMediaQuery(theme => theme.breakpoints.up('sm')) ? 'pc' : 'sp'
}