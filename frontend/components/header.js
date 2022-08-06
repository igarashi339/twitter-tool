import { AppBar, Box, Toolbar, List, ListItem, ListItemText, Typography } from '@mui/material'
import { Menu } from '@mui/icons-material'
import { css } from '@emotion/react'
import { useLayout } from '../hooks'
import { useRouter } from 'next/router'

const toolbarStyle = css`
  /* display: flex; */
  justify-content: space-between;
`

const logoStyle = css`
  width: 140px;
  cursor: pointer;
`

const listStyle = css`
  display: flex;
  justify-content: space-between;
`

const listItemStyle = css`
  padding: 8px;
`

const linkStyle = css`
  cursor: pointer;
  white-space: nowrap;
`

const menu = [
  { text: 'ホーム', path: '/' },
  { text: 'あああ', path: '/aaa' },
  { text: 'いいい', path: '/iii' }
]

export const Header = () => {
  const layout = useLayout()
  return (
    <AppBar position="static">
      <Toolbar css={toolbarStyle}>
        <Box css={logoStyle}>
          <Logo />
        </Box>
        {layout === 'pc' && <PCMenu />}
        {layout === 'sp' && <SPMenu />}
      </Toolbar>
    </AppBar>
  )
}

const Logo = () => {
  const router = useRouter()
  return (
    <Typography onClick={() => router.push('/')}>twitter-tool</Typography>
  )
}

const PCMenu = () => {
  const router = useRouter()
  return (
    <List
      css={listStyle}
    >
      {menu.map((ele, index) => (
        <ListItem css={listItemStyle}key={index}>
          <ListItemText css={linkStyle} onClick={() => router.push(ele.path)}>{ele.text}</ListItemText>
        </ListItem>
      ))}
    </List>
  )
}

const SPMenu = () => {
  return (
    <Menu />
  )
}