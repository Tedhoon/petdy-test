import React from "react";
import { ResponsiveBar } from '@nivo/bar';
// make sure parent container have a defined height when using
// responsive component, otherwise height will be 0 and
// no chart will be rendered.
// website examples showcase many properties,
// you'll often use just a few of them.
const datas = [
    {
      "country": "AD",
      "hot dog": 98,
      "hot dogColor": "hsl(266, 70%, 50%)",
      "burger": 51,
      "burgerColor": "hsl(202, 70%, 50%)",
      "sandwich": 23,
      "sandwichColor": "hsl(41, 70%, 50%)",
      "kebab": 108,
      "kebabColor": "hsl(222, 70%, 50%)",
      "fries": 136,
      "friesColor": "hsl(318, 70%, 50%)",
      "donut": 17,
      "donutColor": "hsl(130, 70%, 50%)"
    },
    {
      "country": "AE",
      "hot dog": 122,
      "hot dogColor": "hsl(230, 70%, 50%)",
      "burger": 13,
      "burgerColor": "hsl(295, 70%, 50%)",
      "sandwich": 5,
      "sandwichColor": "hsl(123, 70%, 50%)",
      "kebab": 77,
      "kebabColor": "hsl(344, 70%, 50%)",
      "fries": 72,
      "friesColor": "hsl(206, 70%, 50%)",
      "donut": 81,
      "donutColor": "hsl(208, 70%, 50%)"
    },
    {
      "country": "AF",
      "hot dog": 39,
      "hot dogColor": "hsl(313, 70%, 50%)",
      "burger": 13,
      "burgerColor": "hsl(121, 70%, 50%)",
      "sandwich": 71,
      "sandwichColor": "hsl(64, 70%, 50%)",
      "kebab": 129,
      "kebabColor": "hsl(260, 70%, 50%)",
      "fries": 114,
      "friesColor": "hsl(104, 70%, 50%)",
      "donut": 73,
      "donutColor": "hsl(299, 70%, 50%)"
    },
    {
      "country": "AG",
      "hot dog": 35,
      "hot dogColor": "hsl(145, 70%, 50%)",
      "burger": 100,
      "burgerColor": "hsl(116, 70%, 50%)",
      "sandwich": 143,
      "sandwichColor": "hsl(115, 70%, 50%)",
      "kebab": 163,
      "kebabColor": "hsl(43, 70%, 50%)",
      "fries": 94,
      "friesColor": "hsl(175, 70%, 50%)",
      "donut": 176,
      "donutColor": "hsl(118, 70%, 50%)"
    },
    {
      "country": "AI",
      "hot dog": 150,
      "hot dogColor": "hsl(285, 70%, 50%)",
      "burger": 100,
      "burgerColor": "hsl(264, 70%, 50%)",
      "sandwich": 156,
      "sandwichColor": "hsl(337, 70%, 50%)",
      "kebab": 90,
      "kebabColor": "hsl(159, 70%, 50%)",
      "fries": 37,
      "friesColor": "hsl(354, 70%, 50%)",
      "donut": 39,
      "donutColor": "hsl(146, 70%, 50%)"
    },
    {
      "country": "AL",
      "hot dog": 179,
      "hot dogColor": "hsl(275, 70%, 50%)",
      "burger": 100,
      "burgerColor": "hsl(256, 70%, 50%)",
      "sandwich": 188,
      "sandwichColor": "hsl(341, 70%, 50%)",
      "kebab": 83,
      "kebabColor": "hsl(358, 70%, 50%)",
      "fries": 29,
      "friesColor": "hsl(135, 70%, 50%)",
      "donut": 50,
      "donutColor": "hsl(45, 70%, 50%)"
    },
    {
      "country": "AM",
      "hot dog": 169,
      "hot dogColor": "hsl(115, 70%, 50%)",
      "burger": 163,
      "burgerColor": "hsl(232, 70%, 50%)",
      "sandwich": 119,
      "sandwichColor": "hsl(159, 70%, 50%)",
      "kebab": 118,
      "kebabColor": "hsl(101, 70%, 50%)",
      "fries": 6,
      "friesColor": "hsl(69, 70%, 50%)",
      "donut": 191,
      "donutColor": "hsl(17, 70%, 50%)"
    }
  ]
console.log(datas)

const NoviGraph = () => (
    <ResponsiveBar
        data={datas}
        keys={[ 'hot dog', 'burger', 'sandwich', 'kebab', 'fries', 'donut' ]}
        indexBy="country"
        margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
        padding={0.3}
        colors={{ scheme: 'nivo' }}
        defs={[
            {
                id: 'dots',
                type: 'patternDots',
                background: 'inherit',
                color: '#38bcb2',
                size: 4,
                padding: 1,
                stagger: true
            },
            {
                id: 'lines',
                type: 'patternLines',
                background: 'inherit',
                color: '#eed312',
                rotation: -45,
                lineWidth: 6,
                spacing: 10
            }
        ]}
        fill={[
            {
                match: {
                    id: 'fries'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'sandwich'
                },
                id: 'lines'
            }
        ]}
        borderColor={{ from: 'color', modifiers: [ [ 'darker', 1.6 ] ] }}
        axisTop={null}
        axisRight={null}
        axisBottom={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: 'country',
            legendPosition: 'middle',
            legendOffset: 32
        }}
        axisLeft={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: 'food',
            legendPosition: 'middle',
            legendOffset: -40
        }}
        labelSkipWidth={12}
        labelSkipHeight={12}
        labelTextColor={{ from: 'color', modifiers: [ [ 'darker', 1.6 ] ] }}
        legends={[
            {
                dataFrom: 'keys',
                anchor: 'bottom-right',
                direction: 'column',
                justify: false,
                translateX: 120,
                translateY: 0,
                itemsSpacing: 2,
                itemWidth: 100,
                itemHeight: 20,
                itemDirection: 'left-to-right',
                itemOpacity: 0.85,
                symbolSize: 20,
                effects: [
                    {
                        on: 'hover',
                        style: {
                            itemOpacity: 1
                        }
                    }
                ]
            }
        ]}
        animate={true}
        motionStiffness={90}
        motionDamping={15}
    />
)

export default NoviGraph;